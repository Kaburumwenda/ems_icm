<template>
	<div class="">
		<div class="uk-grid- uk-grid" data-uk-grid>
			<!-- dynamic fields -->
			<div class="dependant-con">
				<div  class="sc-padding sc-form-section" >
					<div class="uk-grid-match uk-grid" data-uk-grid>
						<div class="uk-width-expand@m">
							<div class="uk-child-width-1-3@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
								<div>
									<ScInput>
										<label>Department</label>
									</ScInput>
								</div>
								<div>
									<ScInput>
										<label>Employment type</label>
									</ScInput>
								</div>
                                <div>
									<ScInput >
										<label>section</label>
									</ScInput>
								</div>
							</div>
							<div class="uk-child-width-1-3@m uk-flex uk-flex-middle" data-uk-grid>
                                <div>
                                    <label>Employment duration <sup>*</sup></label>
                                    <b-form-input placeholder="i.e. 3yrs" required></b-form-input>
                                </div>
								<div>									
									<label>Employment date</label>
									<b-form-datepicker id="example-datepicker-d"></b-form-datepicker>							
								</div>
								<div>									
									<label>Exit date</label>
									<b-form-datepicker id="example-datepicker-d"></b-form-datepicker>							
								</div>
								
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- dynamic fields -->
		</div>

	</div>
</template>

<script>
import jQuery from '~/plugins/jquery'
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
import ScInput from '~/components/Input'
import PrettyRadio from 'pretty-checkbox-vue/radio';
const { uniqueID } = scHelpers;
import PrettyCheck from 'pretty-checkbox-vue/check';
import { scHelpers } from "~/assets/js/utils";

if(process.client) {
	require('~/assets/js/vendor/jquery.creditCardValidator.js');
	require('~/plugins/inputmask');
}

export default {
	name: 'FormsWizardStep4',
	components: {
		PrettyRadio,
		ScInput
	},
	mixins: [validationMixin],
	data: () => ({
		gender:['Male', 'Female', 'Not sure', 'Rather not to say'],	
		userData: {
			paymentMethod: {
				name: '',
				ccNumber: '',
				ccType: ''
			}
		},
		dynamicFields: [
			{
				id: uniqueID(),
				firstName: '',
				lastName: '',
				email: '',
				phoneNumber: '',
				registerUser: false
			}
		],
		
		ccIcon: require('~/assets/img/blank.gif')
	}),
	
	mounted () {
	},
	methods: {
		// addUser (e) {
		// 	e.preventDefault();
		// 	this.dynamicFields.push({
		// 		id: uniqueID(),
		// 		firstName: '',
		// 		lastName: '',
		// 		email: '',
		// 		phoneNumber: '',
		// 		registerUser: false
		// 	})
		// },
		// removeUser (e, id) {
		// 	e.preventDefault();
		// 	var index = this.dynamicFields.map(function (item) {
		// 		return item.id
		// 	}).indexOf(id);
		// 	this.dynamicFields.splice(index, 1);
		// },
		validate () {
			this.$v.userData.paymentMethod.$touch();
			var isValid = !this.$v.userData.paymentMethod.$invalid;
			this.$emit('on-validate', this.$data.userData, isValid);
			return isValid
		},
		// credit cards example numbers
		ccExampleFill (e, number) {
			e.preventDefault();
			$(this.$refs.ccValidateInput).val(number).trigger('input');
			this.userData.paymentMethod.ccNumber = number;
		},
		getCcIcon (name) {
			this.ccIcon = name ? require('~/assets/icons/payment-icons/color/' + name + '.png') : require('~/assets/img/blank.gif')
		}
	}
}
</script>

<style lang="scss">
	@import '~scss/vue/_pretty_checkboxes';
</style>
<style scoped>
.dependant-con{
	background-color: white;
}
label{
	font-size: 18px;
}
</style>