<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-if="showCard">
			<v-card-title>
				<h1 class="headline">パスワード再設定</h1>
			</v-card-title>
			<v-card-text>
				<v-form
					v-model="isValid"
					ref="form"
				>
					<v-text-field
						v-bind:type="showPassword ? 'text' : 'password'"
						prepend-icon="mdi-lock"
						v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
						label="パスワード"
						@click:append="showPassword = !showPassword"
						v-model="password"
						:hint="form.passwordMsg"
						:rules="form.passwordRules"
					/>
					<v-card-actions>
							<v-btn
								:disabled="!isValid || loading"
								:loading="loading"
								class="info ml-auto mt-5"
								@click="submit">
									パスワードを再設定する
							</v-btn>
					</v-card-actions>
				</v-form>
			</v-card-text>
		</v-card>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-else-if="!isError">
			<v-card-title>
				<h1 class="headline">パスワード再設定</h1>
			</v-card-title>
			<v-card-text>
				<p>
					パスワードの再設定を完了しました。
					<br>
					新しいパスワードで再ログインしてください。
				</p>
			</v-card-text>
			<v-btn
				block
				color="secondary"
				elevation="2"
				@click="routeLogin"
			>
				ログイン
			</v-btn>
		</v-card>
	</v-app>
</template>


<script>
	import crypto from 'crypto'
	import axios from 'axios';

	export default{
		name: 'Passreset',
		data(){
			return{
				isValid: false,
				loading: false,
				showPassword: false,
				password: '',
				jwtString: '',
				showCard: true,
				isError: false,
			}
		},
		methods:{
			//クエリストリングのjwtをbase64でデコードしてJSON形式にする
			decodeJwt: function(token){
				var base64Url = token.split('.')[1];
				var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');

				var encodeURI = encodeURIComponent(atob(base64));
				var decodeString = decodeURIComponent(encodeURI);
				return JSON.parse(decodeString);
			},
			submit: function(){
				this.loading = true

				//入力されたパスワードをsha256でハッシュ化する
				let sha256 = crypto.createHash('sha256')
				sha256.update(this.password)
				const hashedPassword = sha256.digest('base64')
				//POSTする際のヘッダー情報にjwtを入れる
				const headers = {
					'Authorization': this.jwtString
				}
				//ハッシュ化したパスワードをPOST
				axios.post("/user/password/reset", {
					'reset_hashed_password':hashedPassword,
				},{headers}
				)
				.then((res) => {
					console.log(res.status);
					if(res.status == 200){
						this.showCard = false
					}
				})
				.catch((err) => {
					console.log(err);
					this.showCard = false
					this.isError = true
				})
			},
			routeLogin: function(){
				this.$router.push('/login')
			}
		},
		created: function(){
			//クエリストリングのjwtを取り出して、定義されてない場合は'hoge'を返す
			let jwt = this.$route.query.jwt != undefined ? this.$route.query.jwt : 'hoge'
			//methods内で使用したいからjwtとメールアドレスを代入
			this.jwtString = 'Bearer ' + jwt
		},
		computed:{
			form () {
				const passwordMsg = '8文字以上。半角英数字と記号が使えます'
				// 入力規則
				const required = v => !!v || ''
				const passwordFormat = v => /^[ -~¥]{8,}$/.test(v) || ''

				const passwordRules = [required,passwordFormat]

				return { passwordRules, passwordMsg }
			}
		}
	}
</script>