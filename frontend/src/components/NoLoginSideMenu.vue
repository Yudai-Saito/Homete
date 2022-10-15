<template>
	<v-container class="sideContainer">
		<v-row justify="start" class="mt-7 sideMenuButton">
			<v-btn
				small
				rounded
				text
				to="/signup/mail"
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
				to="/login"
			>
				<v-icon>
					mdi-login
				</v-icon>
				ログイン
			</v-btn>
		</v-row>
		<v-row
			justify="end"
			align-content="end"
			class="sideMenuUnderButton"
		>
			<v-btn
				small
				rounded
				text
				to="/about"
				class="underButton"
			>
				<v-icon>
					mdi-information-outline
				</v-icon>
				About
			</v-btn>
			<v-btn
				small
				rounded
				text
				class="underButton mb-7"
			>
				<v-icon>
					mdi-clipboard-text-outline
				</v-icon>
				利用規約
			</v-btn>
			<p
				align="end"
				class="versionText"
			>
				HOMETE v1.0.0
			</p>
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
	.sideMenuUnderButton{
		position: relative;
		bottom: 145px;
		width: 100%;
		height: 100%;
		margin-left: auto;
	}
	.underButton{
		margin: 0;
		padding: 0;
		margin-bottom: 5pt;
	}
	.versionText{
		font-size: smaller;
		position: relative;
		top: auto;
		bottom: 0;
		right: 1rem;
	}
</style>

<script>
export default{
	name: 'NoLoginSideMenu',
	data(){
		return{
		}
	},
}
</script>