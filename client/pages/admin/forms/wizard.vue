<template>
	<div id="sc-page-wrapper">
		 <div id="sc-page-top-bar" class="sc-top-bar">
             <div class="sc-top-bar-content uk-flex uk-flex-1">
				<h1 class="sc-top-bar-title uk-flex-1">
					Employee Registration
				</h1>
             
				<span class="uk-text-muted">
					Public
				</span>
				<div class="sc-actions uk-margin-left">
					<a href="javascript:void(0)" class="sc-actions-icon mdi mdi-filter-variant sc-js-el-hide md-color-red-800 uk-animation-shake" data-uk-toggle="target: #sc-page-top-bar; cls: sc-top-bar-expanded"></a>
					<a href="javascript:void(0)" class="sc-actions-icon mdi mdi-close sc-js-el-show" data-uk-toggle="target: #sc-page-top-bar; cls: sc-top-bar-expanded"></a>
				</div>
			</div>
        </div>

<!--- ****************************************************** CONTENT ************************ -->
		<div id="sc-page-content">
			<div class="uk-flex-center uk-grid" data-uk-grid>
				<div class="uk-width-4-5@l">
					<ScCard>
						<ScCardBody>
							<client-only>
								<FormWizard @on-complete="onComplete">
									<TabContent
										title="Employee Info."
										sub-title="Enter employee information."
										
									>
										<Step1 ref="step1" @on-validate="mergePartialModels"></Step1>
									</TabContent>
									<!-- <p>:before-change="()=>validateStep('step1')"</p> -->
									<TabContent
										title="Dependants Info."
										sub-title="Enter dependants Information"
										icon="mdi mdi-credit-card"
									>
									<!-- :before-change="()=>validateStep('step2')" -->
										<Step2 ref="step2" @on-validate="mergePartialModels"></Step2>
									</TabContent>

									<TabContent
										title="next of kin Info."
										sub-title="Enter next`s of kin Information"
										icon="mdi mdi-credit-card"
									>
									<!-- :before-change="()=>validateStep('step3')" -->
										<Step3 ref="step3" @on-validate="mergePartialModels"></Step3>
									</TabContent>

									<TabContent
										title="Employment Info."
										sub-title="Employment Information"
										icon="mdi mdi-credit-card"
									>
									<!-- :before-change="()=>validateStep('step3')" -->
										<Step4 ref="step4" @on-validate="mergePartialModels"></Step4>
									</TabContent>

									<TabContent
										title="Confirmmation"
										sub-title="Verify employee details"
									>
										<Step5 :data="finalModel"></Step5>
									</TabContent>
								</FormWizard>
							</client-only>
						</ScCardBody>
					</ScCard>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import {FormWizard, TabContent } from '~/components/wizard'

export default {
	name: 'FormsWizard',
	layout:"defaultV1",
	components: {
		FormWizard,
		TabContent,
		Step1: process.client ? () => import('./wizard/step1') : null,
		Step2: process.client ? () => import('./wizard/step2') : null,
		Step3: process.client ? () => import('./wizard/step3') : null,
		Step4: process.client ? () => import('./wizard/step4') : null,
		Step5: process.client ? () => import('./wizard/step5') : null,
	},
	data: () => ({
		finalModel: {
			paymentMethod: {}
		}
	}),
	computed: {

	},
	methods: {
		validateStep (name) {
			var refToValidate = this.$refs[name];
			return refToValidate.validate();
		},
		mergePartialModels (model, isValid){
			if(isValid){
				this.finalModel = Object.assign({}, this.finalModel, model)
			}
		},
		onComplete () {
			alert('Done!');
		}
	}
}
</script>

<style lang="scss">
	@import '~scss/plugins/steps.scss';
</style>
