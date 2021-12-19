<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3">
			<v-card-title>
				<h1 class="headline">新規登録</h1>
			</v-card-title>
			<v-card-text>
				<v-form>
                    <v-text-field
						prepend-icon="mdi-account-circle"
						label="ユーザー名"
						v-model="username"
					/>
                    <v-text-field
						prepend-icon="mdi-badge-account-horizontal"
						label="ユーザーId"
						v-model="userid"
					/>
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
								登録
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
		name: 'Signup',
		data(){
			return{
				showPassword: false,
				userEmail: '',
				username: '',
				userid: '',
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
				//入力されたパスワードをsha256でハッシュ化する
				let sha256 = crypto.createHash('sha256')
				sha256.update(this.password)
				const hashPass = sha256.digest('base64')
				//POSTする際のヘッダー情報にjwtを入れる
				const headers = {
					'Authorization': this.jwtString
				}
				//入力された情報に合わせてjwtに含まれてたメールアドレスとハッシュ化したパスワードをPOST
				axios.post("/user/signup", {
					'user_email':this.userEmail,
					'user_name':this.username,
					'user_id':this.userid,
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
		},
		created: function(){
			//クエリストリングのjwtを取り出して、定義されてない場合は'hoge'を返す
			let jwt = this.$route.query.jwt != undefined ? this.$route.query.jwt : 'hoge'
			var decodeJwtString = this.decodeJwt(jwt)
			//methods内で使用したいからjwtとメールアドレスを代入
			this.jwtString = 'Bearer ' + jwt
			this.userEmail = decodeJwtString.sub
		}
	}
</script>
