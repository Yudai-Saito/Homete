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
	export default{
		name: 'Passreset',
		data(){
			return{
				showPassword: false,
				password: '',
			}
		},
		methods:{
		},
	}
</script>