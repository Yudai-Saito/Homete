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
			email: '',
			rescode: true,
		}
	},
	methods: {
		mailsubmit: function() {
			axios.post("/user/signup/mail", {
				'user_email':this.email
			})
			.then((res) => {
				if(res.status==200){
					this.rescode=!this.rescode;
					//通知名'rescode'で親コンポーネントにrescodeを渡す
					this.$emit('rescode',this.rescode)
				}
				console.log(res.status);//res.statusにレスポンスコードが返ってくる
			})
			.catch((err) => {
				console.log(err);
			});
		},
	},
}
</script>