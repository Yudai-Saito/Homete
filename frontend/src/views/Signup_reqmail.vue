<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3">
			<v-card-title>
				<h1 class="headline">新規登録</h1>
				<p><font size="-1">最初に受信可能なメールアドレスを入力してください。</font></p>
			</v-card-title>
			<Requestmail />
		</v-card>
	</v-app>
</template>


<script>
	import Requestmail from '../components/Requestmail'

	export default{
		name: ' Signup_reqmail',
		components: {
			Requestmail,
		},
	}
</script>
