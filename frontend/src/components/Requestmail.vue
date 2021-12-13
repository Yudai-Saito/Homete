<template>
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
					送信
					</v-btn>
			</v-card-actions>
		</v-form>
	</v-card-text>
</template>

<script>
export default{
		name: 'Requestmail',
		data(){
			return{
				email: '',
			}
		},
}
</script>