
<template>
	<div>
        

<!--- ****************************************************** CONTENT ************************ -->
            <div>
           <div class="form-con">
           <b-form>
           <div class="row">
               <div class="col-md-4">
                   <label>Firstname <sup>*</sup></label>
                   <b-form-input placeholder="Enter firstname" required></b-form-input>
               </div>
               <div class="col-md-4">
                   <label>Middlename </label>
                   <b-form-input placeholder="Enter middlename"></b-form-input>
               </div>
               <div class="col-md-4">
                   <label>Lastname <sup>*</sup></label>
                   <b-form-input placeholder="Enter lastname" required></b-form-input>
               </div>
           </div>
           <br>
           <div class="row">
               <div class="col-md-3">
                   <label for="example-datepicker">Date of birth <sup>*</sup></label>
                   <b-form-datepicker id="example-datepicker" class="mb-2"></b-form-datepicker>
               </div>
               <div class="col-md-2">
                   <label>Sex <sup>*</sup></label>
                   <b-form-select  :options="gender"></b-form-select>
               </div>
               <div class="col-md-2">
                   <label>Relationship Status <sup>*</sup></label>
                   <b-form-select  :options="relationship" ></b-form-select>
               </div>
               <div class="col-md-2">
                   <label>Nationality <sup>*</sup></label>
                   <b-form-select :options="countries"></b-form-select>
               </div>
               <div class="col-md-3">
                   <label>Primary mobile number <sup>*</sup></label>
                   <vue-tel-input v-model="value"></vue-tel-input> 
               </div>
           </div>
           <br>
           <div class="row">
               <div class="col-md-3">
                   <label>Alternative mobile number</label>
                   <vue-tel-input v-model="value" required></vue-tel-input> 
               </div>
               <div class="col-md-3" >
                   <label>Primary email address <sup>*</sup></label>
                   <b-form-input placeholder="Primary email" required></b-form-input>
               </div>
               <div class="col-md-3">
                   <label>Work email address</label>
                   <b-form-input placeholder="Enter Work email"></b-form-input>
               </div>
               <div class="col-md-3">
                   <label>Postal address</label>
                   <b-form-input placeholder="Enter Postal address"></b-form-input>
               </div>
           </div>
           <br>
           <div class="row">
               <div class="col-md-3">
                   <label>Residential address <sup>*</sup></label>
                   <b-form-input placeholder="Enter residential address"></b-form-input>
               </div>
               <div class="col-md-3">
                   <label>Permanent address</label>
                   <b-form-input placeholder="Enter permanent address"></b-form-input>
               </div>
               <div class="col-md-3">
                   <label>Personal identification type <sup>*</sup></label>
                   <b-form-select  :options="personal_identification_type"></b-form-select>
               </div>
               <div class="col-md-3">
                   <label>Personal identification number <sup>*</sup></label>
                   <b-form-input placeholder="Enter Personal identification number" required></b-form-input>
               </div>
           </div>
           <br>
<!-- *************************************************************************** dependants info   -->
          <h3><strong><em>Dependants Info.</em></strong></h3>
          <table id="dependants" class="table-bordered display responsive nowrap" style="width:100%">
              <thead>
                  <th>Dependants name</th>
                  <th>Date of birth</th>
                  <th>Sex</th>
                  <th>Relation</th>
                  <th></th>
              </thead>
              <tbody>
                  <tr 
                  v-for="(tr, index) in dependants"
                  :key="`dependantTd-${index}`">
                      <td><b-form-input placeholder="Enter dependants name" required></b-form-input></td>
                      <td><b-form-datepicker id="example-datepicker-d" required></b-form-datepicker></td>
                      <td><b-form-select  :options="gender"></b-form-select></td>
                      <td><b-form-input placeholder="i.e. Mother" required></b-form-input></td>
                      <td class="text-center">
                          <b-icon icon="dash-circle-fill" 
                            v-show="dependants.length > 1"  
                            @click="removeField(index, dependants)" 
                            font-scale="1.5"
                            variant="danger"
                            >
                            </b-icon>          
                      </td>
                  </tr>
              </tbody>
          </table>
          <!--**********-------------------------------------- Incre button container ------************-->
          <div class="dependants-incr-btn">
              <div></div>
              <div>
                  <b-button 
                  variant="primary" 
                  squared 
                  @click="addField(td, dependants)"
                  >
                      <div class="dependants-incr-btn-items">
                          <span class="material-icons menu-s-icon">playlist_add</span>
                          <span style="margin-left:10px">add</span>
                      </div>
                  </b-button>
              </div>
          </div>
          <!--**********-------------------------------------- Incre button container ------************-->
          <div>
         <script>
            
           </script>
          </div>     
<!-- *************************************************************************** dependants info   -->

<!-- *************************************************************************** Next of Kin info   -->
         <h4><strong><em>Next of Kin Info.</em></strong></h4>
         <div style="">
             <table id="exampleaa" class="table table-bordered display dt-responsive  nowrap" style="width:100%">
                 <thead>
                     <tr>
						<th>Name</th>
						<th>Sex</th>
						<th>Relation</th>
						<th>Phone</th>
						<th>Email</th>
						<th>Postal Address</th>
						<th>Permanent Address</th>
						<!-- <th>Action</th> -->
					 </tr>
                 </thead>
                 <tbody>
                     <!-- <tr 
                       v-for="(input, index) in kin"
                      :key="`kinInput-${index}`"
					  
					  >
                         <td><b-form-input placeholder="dependants name" style="width:200px"></b-form-input></td>
                         <td><b-form-select  :options="gender" style="width:100px"></b-form-select></td>
                         <td><b-form-input placeholder="i.e. Mother" style="width:200px"></b-form-input></td>
                         <td><vue-tel-input style="width:250px"></vue-tel-input> </td>
                         <td><b-form-input placeholder="email address" style="width:200px"></b-form-input></td>
                         <td><b-form-input placeholder="postal address" style="width:200px"></b-form-input></td>
                         <td><b-form-input placeholder="permanent address" style="width:200px"></b-form-input></td>
                         <td class="text-center">
								 <b-icon icon="dash-circle-fill" 
                                v-show="kin.length > 1"  
                                @click="removeField(index, kin)" 
                                font-scale="1.5"
                                variant="danger"
                                >
                            </b-icon>  
                         </td>
                     </tr> -->
                 </tbody>
             </table>
         </div>
         <!--**********-------------------------------------- Incre button container ------************-->
          <div class="dependants-incr-btn">
              <div></div>
              <div>
                  <b-button 

                  variant="primary" 
                  squared 
                  @click="addKinField(input, kin)"
                  style="margin-top:5px"
                  >
                      <div class="dependants-incr-btn-items">
                          <span class="material-icons menu-s-icon">playlist_add</span>
                          <span style="margin-left:10px">add</span>
                      </div>
                  </b-button>
              </div>
          </div>
          <!--**********-------------------------------------- Incre button container ------************-->
<!-- *************************************************************************** Next of Kin info   -->

<!-- *************************************************************************** Employment info   -->
       <h4><strong><em>Employment Info.</em></strong></h4>
       <div class="row">
           <div class="col-md-4">
               <label>Department <sup>*</sup></label>
                <b-form-input placeholder="i.e. Sales" required></b-form-input>
           </div>
           <div class="col-md-4">
               <label>Employment type <sup>*</sup></label>
                <b-form-input placeholder="Enter employment type" required></b-form-input>
           </div>
           <div class="col-md-4">
               <label>section</label>
                <b-form-input placeholder="Enter section" required></b-form-input>
           </div>
       </div>
       <br>
       <div class="row">
           <div class="col-md-4">
               <label>Employment duration <sup>*</sup></label>
               <b-form-input placeholder="i.e. 3yrs" required></b-form-input>
           </div>
           <div class="col-md-4">
               <label>Employment date <sup>*</sup></label>
                <b-form-datepicker id="example-datepicker" class="mb-2"></b-form-datepicker>
           </div>
           <div class="col-md-4">
               <label>Exit date <sup>*</sup></label>
                <b-form-datepicker id="example-datepicker" class="mb-2"></b-form-datepicker>
           </div>
       </div>
       <br>
<!-- *************************************************************************** Employment info   -->
       <b-button variant="primary" block type="submit" size="lg"> 
           <div class="emp-submit-btn">
               <span class="material-icons">send</span> 
               <span style="margin-left:10px">Submit</span>
           </div>
        </b-button>
       </b-form>
       </div>
    </div>
<!--************************************************************** CONTENT **************** -->
<!-- DEMO ************* -->
<!-- DEMO ******-->
	</div>
</template>

<script>
import {VueTelInput} from 'vue-tel-input';
import 'vue-tel-input/dist/vue-tel-input.css';
import {countries} from '../../data/countries'

export default {
  components: { VueTelInput },
    name:"Profile",
	 data(){
        return{
            countries,
            value:'',
            country:'',
            gender:['Male', 'Female', 'Not sure', 'Rather not to say'],
            relationship:['Single', 'Married', 'Divorced', 'Complicated', 'Searching'],
            personal_identification_type:['National Identity', 'Passport', 'Military', 'Alien'],
            dependants: [{ name: "", birth:"", sex:"", relation:"" }],
            kin:[{ name: "", sex:"", relation:"", phone:"", email:"", postal:"", address:"" }]
        }
    },
    mounted(){
        this.KinDatatable();
    },
    methods: {
    addField(name, fieldType) {
      fieldType.push({ name: "", birth:"", sex:"", relation:"" });
    //   table.columns.adjust().responsive.recalc();
     this.KinDatatable();
    },
    removeField(index, fieldType) {
      fieldType.splice(index, 1)
    },
    // sendData(){
    //     console.warn(this.phoneNumbers)
    // },
    addKinField(name, fieldType) {
      fieldType.push({ name: "", sex:"", relation:"", phone:"", email:"", postal:"", address:"" });
	  this.KinDatatable();
    },
    KinDatatable(){
		let table = $("#exampleaa").DataTable( {
           paging: false,
		   searching: false,
		   retrieve: true,
		   ordering: false,
		   info: false
        } );
       const tr = $(
           '<tr> <td><input name="" style="width:200px" placeholder="name"></td> <td><input name="" style="width:200px" placeholder="sex"></td> <td><input name="" style="width:200px" placeholder="relation"></td> <td><input name="" style="width:200px" placeholder="phone"></td> <td><input name="" style="width:200px" placeholder="email"></td> <td><input name="" style="width:200px" placeholder="postal address"></td> <td><input name="" style="width:200px" placeholder="permanent address"></td> </tr>'
           );
       table.row.add(tr[0]).draw();
    }
  },
}
</script>


<style scoped>
.form-con{
    background: white;
    padding: 20px 20px 20px 20px;
    border-radius: 10px;
}
label{
    font-weight:500;
    font-size: 18px;
}
sup{
    color: orangered;
    font-weight: bold;
    font-size:medium;
}
.emp-submit-btn{
    display: flex;
    align-items: center;
    justify-content: center;
}
/************************************ DEPENDANT BTN */
.dependants-incr-btn{
    display: flex;
    justify-content: space-between;
}
.dependants-incr-btn-items{
    display: flex;
    align-items: center;
}
.kin-form-tr{
		width: 300px !important;
	}
@media only screen and (max-width: 768px){
}
</style>