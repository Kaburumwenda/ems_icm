
<template>
	<div id="sc-page-wrapper">
		<div id="sc-page-content">
			<MyTable :tabledata="fakedata"/>
		</div>
	</div>
</template>

<script>
export default {
	name: 'TablePage'
}
</script>
<script>
import MyTable from '../components/Components/mytable.vue'
import {dataTableData} from '../data/dynamicTable'
import {AES, enc}from 'crypto-js';
import axios from 'axios';

export default {
  components: { MyTable },
    name:"TablePage",
	layout:'defaultV1',
	data(){
		return{
			dataTable:[],
			fakedata:[],
			secrectKey:'MYKEY4DEMO3R@RTDGH56%RTYF4F4e3#YU'
		}
	},
	mounted(){
		this.getDataTables();
		this.getdecryptedDataTable();
		this.getfakedataapi();
		this.getfakedatalocalstorage();
	},
	methods:{
		getDataTables(){
            var apiData = dataTableData; 
			const tableapiData = AES.encrypt(JSON.stringify(apiData),this.secrectKey);
            localStorage.setItem('tableapiData', tableapiData.toString());
		},
		getdecryptedDataTable(){
			const decrypted2 = AES.decrypt(localStorage.getItem('tableapiData'), this.secrectKey);
		    const decryptedObject = decrypted2.toString(enc.Utf8);
		    var dataq = JSON.parse(decryptedObject)
			this.dataTable=dataq;
		},
		getfakedataapi(){
			this.$axios.$get("/api/v1/fakedata/")
			.then((resp) =>{
				localStorage.setItem("fakeData", JSON.stringify(resp));
			})
		},
		getfakedatalocalstorage(){
			var data = JSON.parse(localStorage.getItem("fakeData"));
			this.fakedata = data;
			console.warn(this.fakedata );
		}
	}
}
</script>