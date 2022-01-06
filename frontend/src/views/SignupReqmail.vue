<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3"  v-if="resFlag"> 
			<v-card-title>
				<h1 class="headline">新規登録</h1>
				<p><font size="-1">最初に受信可能なメールアドレスを入力してください。</font></p>
				
			</v-card-title>
			<!-- Requestmailから'rescode'として渡されてきた表示画面の状態を、渡されたタイミングでnotice_visibleへ引数として渡す -->
			<RequestMail v-on:resCode='noticeVisible' mailUrl="/user/signup/mail"/>
		</v-card>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-else>
			<p>
				ご入力いただいたメールアドレスに確認URLをお送りしました。<br>届いていない場合はページをリロードしてメールアドレスに間違いがないか確認した上で、もう一度送信してください。
			</p>
		</v-card>
	</v-app>
</template>


<script>
	import RequestMail from '../components/RequestMail'
	export default{
		name: 'SignupReqmail',
		data(){
			return{
				resCode: '',
				resFlag: true,
			}
		},
		components: {
			RequestMail,
		},
		methods: {
			//RequestMailから渡されたreqCodeを引数'childRescode'に格納
			noticeVisible: function(childRescode){
				//SignupReqmail内のresCodeにRequestMailのresCodeを代入
				this.resCode = childRescode
				this.resFlag = false
			}
		},
	}
</script>