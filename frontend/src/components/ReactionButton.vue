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
import axios from 'axios';

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
		'postId'
	],
	methods: {
		count: function(){
			if(this.reactionFlag){
				this.reactionCount -= 1
				this.reactionFlag = false

				axios.post('/post/reaction',{
						"post_id":this.postId, "reaction":this.reactionIcon
					},
					{
						withCredentials: true
					
					}
				)
			}
			else{
				this.reactionCount += 1
				this.reactionFlag = true

				axios.put('/post/reaction',{
						post_id: this.postId,
						reaction: this.reactionIcon
					},{
						withCredentials: true
					}
				)
			}
		}
	},
	created() {
		this.postReaction.forEach(item => {
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