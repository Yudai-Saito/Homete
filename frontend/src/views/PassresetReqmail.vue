<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-if="resFlag">
			<v-card-title>
				<h1 class="headline">パスワード再設定</h1>
				<p><font size="-1">ご利用中のメールアドレスを入力してください。<br>パスワード再設定のためのURLをお送りします。</font></p>
			</v-card-title>
			<RequestMail v-on:resCode='noticeVisible' mail-url="/passreset/mail"/>
		</v-card>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-else>
			<p>
				ご入力いただいたメールアドレスにパスワード再設定用URLをお送りしました。<br>届いていない場合はページをリロードしてメールアドレスに間違いがないか確認した上で、もう一度送信してください。
			</p>
		</v-card>
	</v-app>
</template>


<script>
	import RequestMail from '../components/RequestMail'

	export default{
		name: 'PassresetReqmail',
		data(){
			return{
				resFlag: true,
				resCode: '',
			}
		},

		components: {
			RequestMail,
		},
		methods: {
			//RequestMailから渡されたreqCodeを引数'childResCode'に格納
			noticeVisible: function(childResCode){
				//SignupReqmail内のresCodeにRequestMailのresCodeを代入
				this.resCode = childResCode
				console.log(this.resCode)
				this.resFlag = false
			}
		},
	}
</script>
