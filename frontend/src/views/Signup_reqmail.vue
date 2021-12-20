<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3"  v-if="resflag"> 
			<v-card-title>
				<h1 class="headline">新規登録</h1>
				<p><font size="-1">最初に受信可能なメールアドレスを入力してください。</font></p>
				
			</v-card-title>
			<!-- Requestmailから'rescode'として渡されてきた表示画面の状態を、渡されたタイミングでnotice_visibleへ引数として渡す -->
			<Requestmail v-on:rescode='notice_visible' mailUrl="/user/signup/mail"/>
		</v-card>
		<v-card width="400px" class="mx-auto my-auto pa-3" v-else-if="rescode == 200">
			<p>
				ご入力いただいたメールアドレスに確認URLをお送りしました。<br>記載してあるURLをクリックし、ユーザー情報登録へお進みください。
			</p>
		</v-card>
	</v-app>
</template>


<script>
	import Requestmail from '../components/Requestmail'
	export default{
		name: 'Signup_reqmail',
		data(){
			return{
				rescode: '',
				resflag: true,
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