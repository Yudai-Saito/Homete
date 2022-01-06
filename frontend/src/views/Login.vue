<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3">
			<v-card-title class="justify-center cardTitle">
				<h2 class="titleText">Log in</h2>
			</v-card-title>
			<v-card-text>
				<v-form
					v-model="isValid"
					ref="form"
				>
					<v-text-field
						prepend-icon="mdi-email"
						label="ユーザーIDまたはメールアドレス"
						v-model="userInfo"
						:hint="form.userInfoMsg"
						:rules="form.userInfoRules"
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
					<v-card-actions>
						<div class="ic-Login__forgot ml-auto">
							<a class="ic-Login__link forgot_password_link"
								id="login_forgot_password"
								href="PassresetReqmail">
								パスワードを忘れた場合
							</a>
						</div>
					</v-card-actions>
				</v-form>
			</v-card-text>
			<v-btn
				:disabled="!isValid || loading"
				:loading="loading"
				class="ml-auto mr-auto mt-auto loginBtn"
				@click="submit"
				width="400px"
				height="60px"
			>
				Login
			</v-btn>
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
.loginBtn{
	position: relative;
	right: 12px;
	top: 12px;
	border-top-left-radius: 0;
	border-top-right-radius: 0;
}
</style>


<script>
	import crypto from 'crypto';
	import axios from 'axios';

	export default{

		name: 'Login',
		data(){
			return{
				isValid: false,
				loading: false,
				showPassword: false,
				userInfo: '',
				password: '',
			}
		},
		methods:{
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

				//ログイン用にuser_email or user_idとパスワードを送信
				axios.post("/user/login", 
					{
					'user_info':this.userInfo,
					'hashed_password':hashedPassword,
					},
					{
					withCredentials: true
					}
				)
				.then((res) => {
					console.log(res)	
					if (res.status == 200) {
						this.$router.push('/')
					}
					}
				).
				catch((err) => {
					console.log(err);
					}
				)
			},

			formReset(){
				this.userInfo = ''
				this.password = ''	
			},
		},
		computed:{
			form(){
				const userInfoMsg = 'ユーザーIDまたはメールアドレスを入力してください'	
				const passwordMsg = 'パスワードは8文字以上で入力してください'

				const required = v => !!v || ''
				const userInfoFormat = v=>  /^[a-zA-Z_0-9]{1,15}$/.test(v) || /^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/.test(v) || ''
				const passwordFormat = v => /^[ -~¥]{8,}$/.test(v) || ''

				const passwordRules = [required, passwordFormat]
				const userInfoRules = [required, userInfoFormat]

				return { userInfoMsg, passwordMsg, passwordRules, userInfoRules }
			}	
		}
	}
</script>
