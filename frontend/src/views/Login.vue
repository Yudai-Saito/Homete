<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3">
			<v-card-title>
				<h1 class="headline">ログイン</h1>
			</v-card-title>
			<v-card-text>
				<v-form>
					<v-text-field
						prepend-icon="mdi-account-circle"
						label="メールアドレス"
						v-model="email"
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
						<div class="ic-Login__forgot ml-auto">
							<a class="ic-Login__link forgot_password_link"
								id="login_forgot_password"
								href="#">
							パスワードを忘れた場合
							</a>
						</div>
					</v-card-actions>
					<v-card-actions>
							<v-btn
									class="info ml-auto mt-5"
									@click="submit">
							ログイン
							</v-btn>
					</v-card-actions>
				</v-form>
			</v-card-text>
		</v-card>
	</v-app>
</template>


<script>
	export default{
		name: 'Login',
		data(){
			return{
				showPassword: false,
				email: '',
				password: '',
			}
		},
		methods:{
			submit(){
				console.log(this.name,this.password)
			}
		},
	}
</script>
