<template>
	<v-btn
		class="justify-start"
		@click="count"
		elevation='0'
		small
		v-if="!reactionFlag"
	>
		<h2>{{reactionIcon}}</h2>{{reactionCount}}
	</v-btn>
	<v-btn
		class="justify-start pushedButton"
		@click="count"
		elevation='0'
		small
		outlined
		color="#3949AB"
		v-else
	>
		<h2>{{reactionIcon}}</h2>{{reactionCount}}
	</v-btn>
</template>

<style>
	.pushedButton{
		background-color: "#3949AB,0.5";
	}
</style>

<script>
export default{
	name: 'ReactionButton',
	data(){
		return{
			reactionCount: 0,
			reactionFlag: false,
		}
	},
	props:[
		'reactionIcon',
		'postReaction',
		'userReaction',
	],
	methods: {
		count: function(){
			if(this.reactionFlag){
				this.reactionCount -= 1
				this.reactionFlag = false
			}
			else{
				this.reactionCount += 1
				this.reactionFlag = true
			}
		}
	},
	created() {
		this.postReaction.forEach(item => {
			console.log(item)
			if(item.reaction == this.reactionIcon){
				this.reactionCount = item.count - 0
			}
			if(this.userReaction.includes(this.reactionIcon)){
				this.reactionFlag = true
			}
		})
	},
}
</script>