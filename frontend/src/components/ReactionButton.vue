<template>
	<div class="btnDiv">
		<v-btn
			class="d-none d-sm-block grey--text text--darken-3 reactBtn"
			@click="count"
			elevation='0'
			small
			outlined
			v-if="!reactionFlag"
		>
			<h2>{{reactionIcon}}</h2>{{reactionCount}}
		</v-btn>
		<v-btn
			class="d-none d-sm-block pushedButton"
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
			class="d-block d-sm-none grey--text text--darken-3 reactBtn"
			@click="count"
			elevation='0'
			x-small
			outlined
			height="100%"
			width="40px"
			v-if="!reactionFlag"
		>
			<h3>{{reactionIcon}}</h3>{{reactionCount}}
		</v-btn>
		<v-btn
			class="d-block d-sm-none grey--text text--darken-3 pushedButton"
			@click="count"
			elevation='0'
			x-small
			outlined
			height="100%"
			width="40px"
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
		margin-right: 6px;
	}
	.reactBtn{
		background-color:rgba(207, 216, 220, 0.5)
	}
	.reactBtn.v-btn--outlined{
		border: thin solid transparent;
	}
	.pushedButton{
		background-color:rgba(112, 119, 218, 0.5)
	}
	.pushedButton.v-btn--outlined{
		border: thin solid rgb(112, 119, 218);
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