<template>
	<div class="btnDiv">
		<v-btn
			class="d-none d-sm-block reactBtnA justify-start grey--text text--darken-3"
			@click="count"
			elevation='0'
			small
			v-if="!reactionFlag"
		>
			<h2>{{reactionIcon}}</h2>{{reactionCount}}
		</v-btn>
		<v-btn
			class="d-none d-sm-block reactBtnA justify-start pushedButton"
			@click="count"
			elevation='0'
			small
			outlined
			color="#3949AB"
			v-else
		>
			<h2>{{reactionIcon}}</h2>{{reactionCount}}
		</v-btn>

		<v-btn
			class="d-block d-sm-none reactBtnB justify-start grey--text text--darken-3"
			@click="count"
			elevation='0'
			x-small
			v-if="!reactionFlag"
		>
			<h3>{{reactionIcon}}</h3>{{reactionCount}}
		</v-btn>
		<v-btn
			class="d-block d-sm-none reactBtnB justify-start pushedButton"
			@click="count"
			elevation='0'
			x-small
			outlined
			color="#3949AB"
			v-else
		>
			<h3>{{reactionIcon}}</h3>{{reactionCount}}
		</v-btn>
	</div>
</template>
<style>
	.btnDiv{
		margin: 0;
		padding: 0;
	}
	.reactBtnA{
		margin: 0;
		padding: 0;
		margin-right: 6px;
	}
	.reactBtnB{
		margin: 0;
		padding: 0;
		min-height: 22px;
		margin-right: 3px;
	}
	.pushedButton{
		background-color:rgba(207, 216, 220, 0.5)
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