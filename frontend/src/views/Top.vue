<template>
	<v-app>
		<v-overlay
			:value="overlay"
			dark=false
			light=true
		>
			<PostHomete v-on:overlay='noticeVisible' />
		</v-overlay>
		<v-container fluid class="mainContainer mx-auto">
			<v-row justify="center" class="mx-auto">
				<v-col cols="2" class="d-none d-sm-block ma-0 pa-0 leftMenu">
					<SideMenu v-on:overlay='overlayCard' />
				</v-col>

				<v-app-bar
					elevation=0 color=transparent dense class="d-block d-sm-none topMenu"
				>
					<v-app-bar-nav-icon @click="drawer = true" x-large class="d-block d-sm-none navButton"></v-app-bar-nav-icon>
				</v-app-bar>
				<v-navigation-drawer
					v-model="drawer"
					fixed
					temporary
					v-bind:width="150"
				>
					<SideMenu v-on:overlay='overlayCard' />
				</v-navigation-drawer>
				<v-btn elevation=3 fab x-large color="white" icon class="d-block d-sm-none postButton" @click="overlay = true">
					<v-icon>
						mdi-pen-plus
					</v-icon>
				</v-btn>

				<v-divider vertical class="d-none d-sm-block"></v-divider>

				<v-col cols="12" sm="8" md="8" class="subContainer">
					
					<DisplayHomete 
						v-for="post in posts"
						:key="post"
						:postList=post
					/>
				</v-col>

				<v-divider vertical class="d-none d-sm-block"></v-divider>

				<v-col md="2" class="hidden-sm-and-down ma-0 pa-0 rightMenu">
					<h2 align="center">column</h2>
				</v-col>
			</v-row>
		</v-container>
	</v-app>
</template>
<style>
	.testColorA{
		background-color: cyan;
	}
	.testColorB{
		background-color: burlywood;
	}
	.mainContainer{
		max-width: 1200px;
		width: 100%;
		height: 100%;
	}
	.subContainer{
		width: 100%;
	}
	.leftMenu{
		width: 115pt;
		min-width: 115pt;
		max-width: 115pt;
		flex: none;
	}
	.rightMenu{
		min-width: 115pt;
	}
	.topMenu{
		width: 100vw;
		min-width: 100vw;
		max-width: 100vw;
		flex: none;
		margin: 0;
		padding: 0;
	}
	.postButton{
		position: fixed;
		left: 20px;
		bottom: 30px;
		background-color: #1DA1F2;
	}
	.navButton{
		position: fixed;
		left: 30px;
		top: 10px;
	}
</style>


<script>
import PostHomete from '../components/PostHomete'
import DisplayHomete from '../components/DisplayHomete'
import SideMenu  from '../components/SideMenu'

export default {
	name: "Top",
	data(){
		return{
			overlay: false,
			drawer: false,
			posts:[{
				"post_id" : 1,
				"created_at": "2021-12-25T23:32:19",
				"post_content": "絵文字を選んだ!",
				"post_reaction" : [
					{
						"reaction" : "👍",
						"count" : "3"
					},
					{
						"reaction" : "👀",
						"count" : "5"
					}
				],
				"user_reaction" : ["👍", "👀"]
			},
			{
				"post_id" : 2,
				"created_at": "2021-12-25T23:32:19",
				"post_content": "トップ画面ができた!",
				"post_reaction" : [
					{
						"reaction" : "👍",
						"count" : "4"
					}
				],
				"user_reaction" : []
			}],
		}
	},
	components: {
		PostHomete,
		DisplayHomete,
		SideMenu,
	},
	methods: {
		noticeVisible: function(childOverlay){
			this.overlay = childOverlay
			console.log(this.overlay)
		},
		overlayCard: function(childOverlay){
			this.overlay = childOverlay
			this.drawer = false
		}
	},
	mounted(){
		console.log(this.$vuetify.breakpoint)
	},
	created() {
		
	},
};
</script>
