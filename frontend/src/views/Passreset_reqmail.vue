<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3">
			<v-card-title>
				<h1 class="headline">パスワード再設定</h1>
				<p><font size="-1">ご利用中のメールアドレスを入力してください。パスワード再設定のためのURLをお送りします。</font></p>
			</v-card-title>
			<v-card-text>
				<v-form>
					<v-text-field
						prepend-icon="mdi-email"
						label="メールアドレス"
						v-model="email"
					/>
					<v-card-actions>
							<v-btn
								class="info ml-auto mt-5"
								@click="submit">
							再設定メールを送信
							</v-btn>
					</v-card-actions>
				</v-form>
			</v-card-text>
		</v-card>
	</v-app>
</template>


<script>
	export default{
		name: 'Passreset_reqmail',
		data(){
			return{
				email: '',
			}
		},
		methods:{
		},
	}
</script>
