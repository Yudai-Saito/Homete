<template>
	<v-container class="sideContainer">
		<v-row justify="start" class="mt-7 sideMenuButton">
			<v-btn
				small
				rounded
				text
			>
				<v-icon>
					mdi-pen-plus
				</v-icon>
				投稿する
			</v-btn>
		</v-row>
		<v-row justify="start" class="sideMenuButton">
			<v-btn
				small
				rounded
				text
			>
				<v-icon>
					mdi-account-cog
				</v-icon>
				アカウント管理
			</v-btn>
		</v-row>
		<v-row justify="start" class="sideMenuButton">
			<v-btn
				small
				rounded
				text
			>
				<v-icon>
					mdi-logout
				</v-icon>
				ログアウト
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
	name: 'SideMenu',
	data(){
		return{
		}
	},
	methods: {
		
	},
}
</script>