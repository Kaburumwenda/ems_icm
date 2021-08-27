<template>
	<div class="">
		<div class="uk-grid- uk-grid" data-uk-grid>
			<!-- dynamic fields -->
			<div class="dependant-con">
				<div v-for="(item, index) in dynamicFields" :key="item.id" class="sc-padding sc-form-section" :class="{'md-bg-grey-100' : index % 2}">
					<div class="uk-grid-match uk-grid" data-uk-grid>
						<div class="uk-width-expand@m">
							<div class="uk-child-width-1-2@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
								<div>
									<ScInput v-model="item.firstName">
										<label>Name</label>
									</ScInput>
								</div>
								<div>
									<ScInput v-model="item.lastName">
										<label>Relation</label>
									</ScInput>
								</div>
							</div>
							<div class="uk-child-width-1-2@m uk-flex uk-flex-middle" data-uk-grid>
								<div>									
									<label>Date of birth</label>
									<b-form-datepicker id="example-datepicker-d"></b-form-datepicker>							
								</div>
								<div>
									<label>Sex</label>
									<b-form-select  :options="gender"></b-form-select>
								</div>
								
							</div>
						</div>
						<div class="uk-width-auto@m uk-flex-middle">
							<a v-if="dynamicFields.length === (index + 1)" href="javascript:void(0)" class="sc-button sc-button-icon sc-button-outline sc-button-outline-square sc-button-outline-primary" @click="addUser($event)">
								<i class="mdi mdi-plus"></i>
							</a>
							<a v-if="dynamicFields.length !== (index + 1)" href="javascript:void(0)" class="sc-button sc-button-icon sc-button-outline sc-button-outline-square sc-button-outline-danger" @click="removeUser($event,item.id)">
								<i class="mdi mdi-trash-can-outline"></i>
							</a>
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
	name: 'FormsWizardStep2',
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
		addUser (e) {
			e.preventDefault();
			this.dynamicFields.push({
				id: uniqueID(),
				firstName: '',
				lastName: '',
				email: '',
				phoneNumber: '',
				registerUser: false
			})
		},
		removeUser (e, id) {
			e.preventDefault();
			var index = this.dynamicFields.map(function (item) {
				return item.id
			}).indexOf(id);
			this.dynamicFields.splice(index, 1);
		},
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

