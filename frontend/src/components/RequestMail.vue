<template>
	<v-card-text>
		<v-form
			v-model="isValid"
			ref="form"
		>
			<v-text-field
				prepend-icon="mdi-email"
				label="メールアドレス"
				v-model="userEmail"
				:rules="rules"
				placeholder="username@example.com"
			/>
			<v-card-actions>
					<v-btn
						:disabled="!isValid || loading"
						:loading="loading"
						class="info ml-auto mt-5"
						@click="submit">
							送信
					</v-btn>
			</v-card-actions>
		</v-form>
	</v-card-text>
</template>

<script>
import axios from 'axios';
export default{
	name: 'RequestMail',
	data(){
		return{
			isValid: false,
			loading: false,
			userEmail: '',
			// 入力規則
			rules:[
				v => !!v || '',
				v => /^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/.test(v) || '',
			]
		}
	},
	props:[
		'mailUrl'
	],
	methods: {
		submit: function() {
			this.loading = true
			axios.post(this.mailUrl, {
				'user_email':this.userEmail
			})
			.then((res) => {
				//通知名'resCode'で親コンポーネントにresCodeを渡す
				this.$emit('resCode',res.status)
			})
			.catch((err) => {
				console.log(err)
				this.$emit('resCode',err.response.status)
			});
		},
	},
}
</script>