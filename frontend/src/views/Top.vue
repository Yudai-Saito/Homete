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

				<v-divider vertical></v-divider>

				<v-col cols="12" sm="8" md="8" class="subContainer">
					
					<DisplayHomete />
				</v-col>

				<v-divider vertical></v-divider>

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
		}
	},
	mounted(){
		console.log(this.$vuetify.breakpoint)
	}	
};
</script>
