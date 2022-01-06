<template>
	<v-container class="sideContainer">
		<v-row justify="start" class="mt-7 sideMenuButton">
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
				@click="logout"
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
					this.$router.push('/')
				}
			}).catch(err => {
				console.log(err)
			})
		}
	},
}
</script>