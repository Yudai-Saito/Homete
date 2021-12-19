<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-if="resflag">
			<v-card-title>
				<h1 class="headline">パスワード再設定</h1>
				<p><font size="-1">ご利用中のメールアドレスを入力してください。<br>パスワード再設定のためのURLをお送りします。</font></p>
			</v-card-title>
			<Requestmail v-on:rescode='notice_visible'/>
		</v-card>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-else-if="rescode == 200">
			<p>
				ご入力いただいたメールアドレスにパスワード再設定用URLをお送りしました。<br>届いていない場合はメールアドレスに間違いがないか確認し、もう一度送信してください。
			</p>
		</v-card>
	</v-app>
</template>


<script>
	import Requestmail from '../components/Requestmail'

	export default{
		name: 'Passreset_reqmail',
		data(){
			return{
				resflag: true,
				rescode: '',
			}
		},

		components: {
			Requestmail,
		},
		methods: {
			//Requestmailから渡されたreqcodeを引数'child_rescode'に格納
			notice_visible: function(child_rescode){
				//Signup_reqmail内のrescodeにRequestmailのrescodeを代入
				this.rescode = child_rescode
				console.log(this.rescode)
				this.resflag = false
			}
		},
	}
</script>
