<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3">
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
				setTimeout(() => {
					this.formReset()
					this.loading = false
				}, 1500)
				//入力されたパスワードをsha256でハッシュ化する
				let sha256 = crypto.createHash('sha256')
				sha256.update(this.password)
				const hashedPassword = sha256.digest('base64')
				//POSTする際のヘッダー情報にjwtを入れる
				const headers = {
					'Authorization': this.jwtString
				}
				//ハッシュ化したパスワードをPOST
				axios.post("/passward/reset", {
					'hashed_password':hashedPassword,
				},{headers}
				)
				.then((res) => {
					console.log(res.status);
				})
				.catch((err) => {
					console.log(err);
				})
			},
			formReset () {
				this.$refs.form.reset()
				this.params = { password: ''}
			},
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