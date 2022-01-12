<template>
	<v-container
		class="sideContainer"
	>
		<v-row
			justify="start"
			class="mt-7 sideMenuButton"
		>
			<v-btn
				small
				rounded
				text
				@click="visibleCard"
			>
				<v-icon>
					mdi-pen-plus
				</v-icon>
				投稿する
			</v-btn>
		</v-row>
		<v-row
			justify="start"
			class="sideMenuButton"
		>
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
		<v-row
			justify="start"
			class="sideMenuButton"
		>
			<v-btn
				small
				rounded
				text
				@click="logout"
			>
				<v-icon>
					mdi-logout
				</v-icon>
				ログアウト
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
				href="About"
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
		position: relative;
		z-index: 100;
		margin-bottom: 5pt;
	}
	.sideMenuUnderButton{
		position: relative;
		z-index: 10;
		width: 100%;
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
import axios from 'axios';

export default{
	name: 'SideMenu',
	data(){
		return{
			overlay: true,
		}
	},
	methods: {
		visibleCard: function(){
            this.$emit('overlay', this.overlay)
		},
		logout: function(){
			axios.post("/user/logout",
				{
					//
				},{
					withCredentials: true
				}
			).then((res) => {
				console.log(res)
				if (res.status == 200) {
					this.$emit('logout')
				}
			}).catch((err) => {
				console.log(err)
			})
		}
	},
}
</script>