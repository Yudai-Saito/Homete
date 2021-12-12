<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3">
			<v-card-title>
				<h1 class="headline">新規登録</h1>
			</v-card-title>
			<v-card-text>
				<v-form>
					<v-text-field
						prepend-icon="mdi-email"
						label="メールアドレス"
						v-model="email"
					/>
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
                    <v-text-field
						v-bind:type="showPasswordConfirmation ? 'text' : 'password'"
						prepend-icon="mdi-lock"
						v-bind:append-icon="showPasswordConfirmation ? 'mdi-eye' : 'mdi-eye-off'"
						label="パスワード確認"
						@click:append="showPasswordConfirmation = !showPasswordConfirmation"
						v-model="password_confirmation"
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
	export default{
		name: 'Signup',
		data(){
			return{
				showPassword: false,
                showPasswordConfirmation: false,
				email: '',
                username: '',
                userid: '',
				password: '',
                password_confirmation: '',
			}
		},
		methods:{
		},
	}
</script>
