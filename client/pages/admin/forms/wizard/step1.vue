<template>
	<div class="sc-border sc-round sc-padding md-bg-grey-50">
		<div class="uk-grid-medium uk-grid" data-uk-grid>
			<div class="uk-width-expand@l">
				<div class="sc-input-match-field" :class="{'vuelidate-wrapper-error': $v.userData.userTitle.$error}">
					<span class="uk-margin-right">
						<PrettyRadio v-model.trim="userData.userTitle" value="mr" class="p-radio" name="userTitle">
							Mr.
						</PrettyRadio>
					</span>
					<span>
						<PrettyRadio v-model.trim="userData.userTitle" value="mrs" class="p-radio" name="userTitle">
							Mrs.
						</PrettyRadio>
					</span>
				</div>
				<ul class="sc-vue-errors">
					<li v-if="!$v.userData.userTitle.required">
						Field is required
					</li>
				</ul>
			</div>
			<div class="uk-width-2-5@l uk-width-1-2@m">
				<ScInput v-model.trim="userData.firstName" name="userData.firstName" :error-state="$v.userData.firstName.$error" :validator="$v.userData.firstName">
					<label>First Name *</label>
				</ScInput>
				<ul class="sc-vue-errors">
					<li v-if="!$v.userData.firstName.required">
						Field is required
					</li>
					<li v-if="!$v.userData.firstName.minLength">
						First Name must have at least {{ $v.userData.firstName.$params.minLength.min }} letters.
					</li>
				</ul>
			</div>
			<div class="uk-width-2-5@l uk-width-1-2@m">
				<ScInput v-model.trim="userData.lastName" name="lastName" :error-state="$v.userData.lastName.$error" :validator="$v.userData.lastName">
					<label>last Name *</label>
				</ScInput>
				<ul class="sc-vue-errors">
					<li v-if="!$v.userData.lastName.required">
						Field is required
					</li>
				</ul>
			</div>
		</div>


		<div class="uk-child-width-1-3@s uk-margin uk-grid" data-uk-grid>
			<div>
				<ScInput v-model.trim="userData.email" name="email" :error-state="$v.userData.email.$error" :validator="$v.userData.email">
					<label>Email *</label>
				</ScInput>
				<ul class="sc-vue-errors">
					<li v-if="!$v.userData.email.required">
						Field is required
					</li>
					<li v-if="!$v.userData.email.email">
						This value should be a valid email
					</li>
				</ul>
			</div>
			<div>
				<ScInput v-model.trim="userData.workemail">
					<label>work email</label>
				</ScInput>
			</div>
			<div>
				<label>Primary mobile number <sup>*</sup></label>
                <vue-tel-input v-model.trim="userData.phoneNumber"></vue-tel-input> 
			</div>
		</div>

		<div class="uk-child-width-1-3@s uk-margin uk-grid" data-uk-grid>
			<div>
				<label>Alternative mobile number</label>
                <vue-tel-input v-model.trim="userData.phoneNumber2"></vue-tel-input> 
			</div>
			<div>
				<label for="example-datepicker">Date of birth <sup>*</sup></label>
                <b-form-datepicker id="example-datepicker" class="mb-2"></b-form-datepicker>
			</div>
			<div>
				<label>Relationship Status <sup>*</sup></label>
                <b-form-select  :options="relationship" ></b-form-select>
			</div>
		</div>


		<div class="uk-child-width-1-2@s uk-margin uk-grid" data-uk-grid>
			<div>
				<label>Postal address</label>
                   <b-form-input placeholder="Enter Postal address"></b-form-input>
			</div>
			<div>
				<label>Nationality <sup>*</sup></label>
                <b-form-select :options="countriesa"></b-form-select>
			</div>		
		</div>
		
	</div>
</template>


<script>
import {VueTelInput} from 'vue-tel-input';
import 'vue-tel-input/dist/vue-tel-input.css';
import {countriesa} from '~/data/countries';

import { scHelpers } from "~/assets/js/utils";
const { uniqueID } = scHelpers;

const countries = require('~/data/common/countries.json');
const usCities = require('~/data/common/us_cities.json');

import ScInput from '~/components/Input'
import PrettyRadio from 'pretty-checkbox-vue/radio';
import { validationMixin } from 'vuelidate'
import { required, minLength, email } from 'vuelidate/lib/validators'
import customValidators from '~/plugins/vuelidateValidators'

if(process.client) {
	require('~/plugins/inputmask')
}

export default {
	name: 'FormsWizardStep1',
	components: {
		PrettyRadio,
		VueTelInput,
		ScInput,
		Select2: process.client ? () => import('~/components/Select2') : null
	},
	mixins: [validationMixin],
	data: () => ({
		 value:'',
		 countriesa,
            country:'',
            gender:['Male', 'Female', 'Not sure', 'Rather not to say'],
            relationship:['Single', 'Married', 'Divorced', 'Complicated', 'Searching'],
            personal_identification_type:['National Identity', 'Passport', 'Military', 'Alien'],
            dependants: [{ name: "", birth:"", sex:"", relation:"" }],
            kin:[{ name: "", sex:"", relation:"", phone:"", email:"", postal:"", address:"" }],

		userData: {
			userTitle: '',
			firstName: '',
			lastName: '',
			email: '',
			workemail:'',
			phoneNumber: '',
			phoneNumber2:'',
			company: '',
			companyID: '',
			addresses: [
				{
					id: uniqueID(10),
					billingAddress: '',
					zipCode: '',
					city: '',
					country: '',
				}
			]
		}
	}),
	computed: {
		countries () {
			return countries.map(function (obj) {
				obj.id = obj.id || obj.code;
				obj.text = obj.text || obj.name;
				return obj;
			});
		},
		usCities () {
			return usCities.map(function (obj) {
				obj.id = obj.id || obj.rank;
				obj.text = obj.text || obj.city;
				return obj;
			});
		}
	},
	validations: {
		userData: {
			userTitle: {
				required
			},
			firstName: {
				required,
				minLength: minLength(3)
			},
			lastName: {
				required
			},
			email: {
				required,
				email
			}
		}
	},
	methods: {
		validate () {
			this.$v.userData.$touch();
			var isValid = !this.$v.userData.$invalid;
			this.$emit('on-validate', this.$data.userData, isValid);
			return isValid
		},
		addAddress (e) {
			e.preventDefault();
			this.userData.addresses.push({
				id: uniqueID(10),
				billingAddress: '',
				zipCode: '',
				city: '',
				country: '',
			});
		},
		removeAddress (e, id) {
			e.preventDefault();
			var index = this.userData.addresses.map(function (item) {
				return item.id
			}).indexOf(id);
			this.userData.addresses.splice(index, 1);
		},
	}
}
</script>

<style lang="scss">
	@import '~scss/vue/_pretty_checkboxes';
</style>
