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
				<ul class="horizontalListWide d-none d-sm-block">
					<li
						v-for="reaction in reactions"
						:key="reaction"
					>
						<ReactionButton
							:reactionIcon=reaction
							:postReaction=postList.post_reaction
							:userReaction=postList.user_reaction
							:postId=postList.post_id
						/>
					</li>
				</ul>
				<ul class="horizontalList d-block d-sm-none">
					<li
						v-for="reaction in reactions"
						:key="reaction"
					>
						<ReactionButton
							:reactionIcon=reaction
							:postReaction=postList.post_reaction
							:userReaction=postList.user_reaction
							:postId=postList.post_id
						/>
					</li>
				</ul>
			</v-card-actions>
		</v-card>
	</v-container>
</template>
<style>
	.horizontalListWide {
		overflow: auto;

		white-space: pre-line;
		-webkit-overflow-scrolling: touch;
		padding: 0;
		margin: 0;
	}
	.horizontalListWide li {
		/* 横スクロール用 */
		position: relative;
		display: inline-block;
		right: 1em;
	}
	.horizontalList {
		overflow-x: auto;
		/* IE, Edge 対応 */
		-ms-overflow-style: none;
		/* Firefox 対応 */
		scrollbar-width: none;

		white-space: nowrap;
		-webkit-overflow-scrolling: touch;
		padding: 0;
		margin: 0;
	}
	/* Chrome, Safari 対応 */
	.horizontalList::-webkit-scrollbar {
		display:none;
	}
	.horizontalList li {
		/* 横スクロール用 */
		position: relative;
		display: inline-block;
		right: 1em;
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