<template>
	<v-container fluid>
		<v-card
			outlined
		>
			<h4 class="ml-4 mt-2">匿名さん</h4>
			<v-divider class="mx-4"></v-divider>
			<v-card-text class="black--text">
				{{homete}}
			</v-card-text>
			<v-card-actions>
				<ReactionButton
					v-for="reaction in reactions"
					:key="reaction"
					:reactionIcon=reaction
					:postReaction=postList.post_reaction
					:userReaction=postList.user_reaction
				/>
			</v-card-actions>
		</v-card>
	</v-container>
</template>
<style>
	.textColor{
		color: red;
	}
</style>

<script>
import ReactionButton from '../components/ReactionButton'
export default{
	name: 'DisplayHomete',
	data(){
		return{
			homete: '',
			reactions: ["👍","👀","💯","🥰","🎉"],
			reactionFlag: false,
		}
	},
	props:[
		'postList'
	],
	components:{
		ReactionButton,
	},
	methods: {
		
	},
	created() {
		this.homete=this.postList.post_content,
		this.reaction=this.postList.post_reaction.reaction
		this.reactionFlag=(this.postList.user_reaction.contains(this.postList.post_reaction))
	},
}
</script>