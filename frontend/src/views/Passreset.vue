<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3">
			<v-card-title>
				<h1 class="headline">パスワード再設定</h1>
			</v-card-title>
			<v-card-text>
				<v-form>
					<v-text-field
						v-bind:type="showPassword ? 'text' : 'password'"
						prepend-icon="mdi-lock"
						v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
						label="パスワード"
						@click:append="showPassword = !showPassword"
						v-model="password"
					/>
					<v-card-actions>
							<v-btn
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
				showPassword: false,
				password: '',
				userEmail: '',
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
				//入力されたパスワードをsha256でハッシュ化する
				let sha256 = crypto.createHash('sha256')
				sha256.update(this.password)
				const hashPass = sha256.digest('base64')
				//POSTする際のヘッダー情報にjwtを入れる
				const headers = {
					'Authorization': this.jwtString
				}
				//入力された情報に合わせてjwtに含まれてたメールアドレスとハッシュ化したパスワードをPOST
				axios.post("/passward/reset", {
					'user_email':this.userEmail,
					'hashed_password':hashPass,
				},{headers}
				)
				.then((res) => {
					console.log(res.status);
				})
				.catch((err) => {
					console.log(err);
				})
			}
		}
	}
</script>