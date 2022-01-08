<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-if="showCard">
			<v-card-title class="justify-center cardTitle">
				<h2 class="titleText">Sign up</h2>
			</v-card-title>
			<v-card-text>
				<v-form
					v-model="isValid"
					ref="form"
				>
                    <v-text-field
						prepend-icon="mdi-account-circle"
						label="ユーザー名"
						v-model="userName"
						placeholder="UserName"
						:hint="form.userNameMsg"
						:rules="form.userNameRules"
					/>
                    <v-text-field
						prepend-icon="mdi-badge-account-horizontal"
						label="ユーザーId"
						v-model="userId"
						placeholder="UserId"
						:hint="form.userIdMsg"
						:rules="form.userIdRules"
					/>
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
				</v-form>
			</v-card-text>
			<v-btn
				:disabled="!isValid || loading"
				:loading="loading"
				class="ml-auto mr-auto mt-auto signupBtn"
				@click="submit"
				width="400px"
				height="60px"
			>
				Sign up
			</v-btn>
		</v-card>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-else-if="!isError">
			<v-card-title>
				<h1 class="headline">ようこそ</h1>
			</v-card-title>
			<v-card-text>
				<p>
					アカウントの登録が完了しました。
					<br>
					下記のボタンからログインをしてご利用ください。
				</p>
				<v-btn
					block
					color="secondary"
					elevation="2"
					@click="routeLogin"
				>
					Log in
				</v-btn>
			</v-card-text>
		</v-card>
	</v-app>
</template>

<style>
.titleText{
	font-weight: 400;
}
.cardTitle{
	margin-bottom: 10px;
	width: 95%;
	margin-right: auto;
	margin-left: auto;
	border-bottom: solid thin #CFD8DC;
}
.signupBtn{
	position: relative;
	right: 12px;
	top: 12px;
	border-top-left-radius: 0;
	border-top-right-radius: 0;
}
</style>

<script>
	import crypto from 'crypto'
	import axios from 'axios';

	export default{
		name: 'Signup',
		data(){
			return{
				isValid: false,
				loading: false,
				showPassword: false,
				userEmail: '',
				userName: '',
				userId: '',
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
				//入力された情報に合わせてjwtに含まれてたメールアドレスとハッシュ化したパスワードをPOST
				axios.post("/user/signup", {
					'user_name':this.userName,
					'user_id':this.userId,
					'hashed_password':hashedPassword,
				},{headers}
				)
				.then((res) => {
					console.log(res.status);
					this.showCard = false
				})
				.catch((err) => {
					console.log(err);
					this.showCard = true
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
			var decodeJwtString = this.decodeJwt(jwt)
			//methods内で使用したいからjwtとメールアドレスを代入
			this.jwtString = 'Bearer ' + jwt
			this.userEmail = decodeJwtString.sub
		},
		computed:{
			form () {
				const userNameMsg = '1文字以上16文字未満'
				const userIdMsg = '1文字以上16文字未満。半角英数字と_が使えます'
				const passwordMsg = '8文字以上。半角英数字と記号が使えます'
				// 入力規則
				const required = v => !!v || ''
				const userNameFormat = v => /^[\w\W]{1,15}$/.test(v) || ''
				const userIdFormat = v => /^[a-zA-Z_0-9]{1,15}$/.test(v) || ''
				const passwordFormat = v => /^[ -~¥]{8,}$/.test(v) || ''

				const userNameRules = [required,userNameFormat]
				const userIdRules = [required,userIdFormat]
				const passwordRules = [required,passwordFormat]

				return { userNameRules, userIdRules, passwordRules, userNameMsg, userIdMsg, passwordMsg }
			}
		}
		
	}
</script>
