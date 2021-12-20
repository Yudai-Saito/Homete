<template>
	<v-card-text>
		<v-form
			v-model="isValid"
			ref="form"
		>
			<v-text-field
				prepend-icon="mdi-email"
				label="メールアドレス"
				v-model="email"
				:rules="rules"
				placeholder="username@example.com"
			/>
			<v-card-actions>
					<v-btn
						:disabled="!isValid || loading"
						:loading="loading"
						class="info ml-auto mt-5"
						@click="mailsubmit">
							送信
					</v-btn>
			</v-card-actions>
		</v-form>
	</v-card-text>
</template>

<script>
import axios from 'axios';
export default{
	name: 'Requestmail',
	data(){
		return{
			isValid: false,
			loading: false,
			email: '',
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
		mailsubmit: function() {
			this.loading = true
			setTimeout(() => {
				this.formReset()
				this.loading = false
			}, 1500)
			axios.post(this.mailUrl, {
				'user_email':this.email
			})
			.then((res) => {
				//通知名'rescode'で親コンポーネントにrescodeを渡す
				this.$emit('rescode',res.status)
				console.log(res.status);//res.statusにレスポンスコードが返ってくる
			})
			.catch((err) => {
				this.$emit('rescode',err.response.status)
				console.log(err);
			});
		},
		formReset () {
			this.$refs.form.reset()
			this.params = { email: ''}
		},
	},
}
</script>