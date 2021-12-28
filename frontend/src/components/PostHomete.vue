<template>
	<v-container fluid>
		<v-card
			:loading="loading"
			:disabled="form || loading"
			outlined
		>
			<v-btn
				icon
				plain
				@click="closeCard"
				class="my-1 ml-1"
			>
				<v-icon
					color="black"
				>
					mdi-close
				</v-icon>
			</v-btn>
			<template slot="progress">
				<v-progress-linear
					color="deep-purple"
					height="10"
					indeterminate
				></v-progress-linear>
			</template>
			<v-form
				v-model="isValid"
				ref="form"
			>
				<v-btn
					icon
					plain
					@click="clearText"
					class="float-right mt-2 mr-2"
					v-show="clearVisible"
				>
					<v-icon
						small
						color="glay"
					>
						mdi-close-circle
					</v-icon>
				</v-btn>
				<v-textarea
					label="なにを褒めてもらう？"
					solo
					flat
					auto-grow
					rows="3"
					v-model="homete"
					@input="inputText"
					counter=100	
					:rules="forms.inputRules"
				></v-textarea>
				<v-divider class="mx-4"></v-divider>
				<v-card-actions>
						<v-btn
							:disabled="!isValid || loading"
							class="info ml-auto"
							@click="submit"
							elevation='0'
							rounded
						>
								投稿する
						</v-btn>
				</v-card-actions>
			</v-form>
		</v-card>
	</v-container>
</template>

<script>
export default{
	name: 'PostHomete',
	data(){
		return{
			isValid: false,
			form: false,
			loading: false,
			homete: '',
			clearVisible: false,
			cardVisible: false,
		}
	},
	methods: {
		submit: function() {
			this.loading = true
			setTimeout(() => {
				this.formReset()
				this.loading = false
			}, 1500)
		},
		formReset () {
			this.$refs.form.reset()
			this.params = { homete: ''}
		},
		inputText: function(){
			if(this.clearVisible == false){
				this.clearVisible = true
			}
			else if(this.homete == ''){
				this.clearVisible = false
			}
		},
		clearText: function(){
			this.homete = ''
			this.clearVisible = false
		},
		closeCard: function(){
			this.$emit('cardVisible',this.cardVisible)
		}
	},
	computed:{
		forms(){
			const required = v => !!v || ''
			const inputFormat = v => v.length <= 100 || '100文字以下で入力してください！'

			const inputRules = [required, inputFormat]

			return { inputRules }
		}
	}
}
</script>