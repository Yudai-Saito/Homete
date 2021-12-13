<template>
	<v-app>
		<v-card width="400px" class="mx-auto my-auto pa-3">
			<v-card-title>
				<h1 class="headline">パスワード再設定</h1>
				<p><font size="-1">ご利用中のメールアドレスを入力してください。<br>パスワード再設定のためのURLをお送りします。</font></p>
			</v-card-title>
			<Requestmail />
		</v-card>
	</v-app>
</template>


<script>
	import Requestmail from '../components/Requestmail'

	export default{
		name: 'Passreset_reqmail',
		components: {
			Requestmail,
		},
	}
</script>
