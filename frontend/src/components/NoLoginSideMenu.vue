<template>
	<v-container class="sideContainer">
		<v-row justify="start" class="mt-7 sideMenuButton">
			<v-btn
				small
				rounded
				text
				href="/signup/mail"
			>
				<v-icon>
					mdi-account-plus
				</v-icon>
				新規登録
			</v-btn>
		</v-row>
		<v-row justify="start" class="sideMenuButton">
			<v-btn
				small
				rounded
				text
				href="/login"
			>
				<v-icon>
					mdi-login
				</v-icon>
				ログイン
			</v-btn>
		</v-row>
	</v-container>
</template>
<style>
	.sideContainer{
		height: 100vh;
	}
	.sideMenuButton{
		margin-bottom: 5pt;
	}
</style>

<script>
export default{
	name: 'NoLoginSideMenu',
	data(){
		return{
		}
	},
	methods: {

	},
}
</script>