<template>
    <div>
        <div id="sc-page-wrapper">
        <!-- Top navigation ***************** start *************-->
        <div id="sc-page-top-bar" class="sc-top-bar">
             <div class="sc-top-bar-content uk-flex uk-flex-1">
				<h1 class="sc-top-bar-title uk-flex-1">
					Countries
				</h1>

                <b-button variant="light" id="show-btn" @click="modalShow = !modalShow">
                    <div class="modal-add-btn-initi">
                        <span class="material-icons">add</span>
                        <span>Add</span>
                    </div>
                </b-button>
                <!-- <button class="sc-button uk-margin-small-right" type="button" data-uk-toggle="target: #modal-close-default">
				  Add
				</button> -->
                <!-- <DcModal buttonType="modal"/> -->
             
				<span class="uk-text-muted">
					Public
				</span>
				<div class="sc-actions uk-margin-left">
					<a href="javascript:void(0)" class="sc-actions-icon mdi mdi-filter-variant sc-js-el-hide md-color-red-800 uk-animation-shake" data-uk-toggle="target: #sc-page-top-bar; cls: sc-top-bar-expanded"></a>
					<a href="javascript:void(0)" class="sc-actions-icon mdi mdi-close sc-js-el-show" data-uk-toggle="target: #sc-page-top-bar; cls: sc-top-bar-expanded"></a>
				</div>
			</div>
        </div>
        <!--******************************* ADD MODAL ******************* -->
         
             <b-modal v-model="modalShow" hide-footer centered title="Add Country">
                <div class="d-block">
                    <form>
                        <div>
                            <label><strong>Country name</strong></label>
                            <input class="form-control" type="text">
                        </div>
                        <div>
                            <label><strong>Country code</strong></label>
                            <input class="form-control" type="text">
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-md-6">
                                <b-button variant="primary" block squared="squared">Save and Add another</b-button>
                            </div>
                            <div class="col-md-6">
                                <b-button variant="primary" block squared="squared">Save</b-button>
                            </div>
                        </div>
                    </form>
                </div>
             </b-modal>
             <div id="modal-close-default" class="uk-modal" data-uk-modal>
                <div class="uk-modal-dialog uk-modal-body">
                    <button class="uk-modal-close-default" type="button" data-uk-close></button>
                    <h2 class="uk-modal-title">
                        Add Country
                    </h2>
                    <form>
                        <div>
                            <label>Country name</label>
                            <input class="form-control" type="text">
                        </div>
                        <div>
                            <label>Country code</label>
                            <input class="form-control" type="text">
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-md-6">
                                <b-button variant="primary" block squared="squared">Save and Add another</b-button>
                            </div>
                            <div class="col-md-6">
                                <b-button variant="primary" block squared="squared">Save</b-button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
       
        <!-- *******************************ADD MODAL END *******-->
        <!-- Top Navigation ****************** end ************ -->
		<div id="sc-page-content">
        <div class="country-td-con">
            <table id="exampleaa" class="table table-bordered table-hover">
                <thead>
                    <th>Country name</th>
                    <th>Country code</th>
                    <th></th>
                </thead>
                <tbody>
                    <tr>
                        <td> Kenya </td>
                        <td> KE </td>
                        <td>
                            <b-button variant="danger" size="sm"><span class="material-icons">delete_forever</span></b-button>
                            <b-button variant="primary" size="sm"><span class="material-icons">edit_note</span></b-button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        </div>
	</div>
    </div> 
</template>

<script>
import DcModal from '../../components/Components/button.vue'

export default {
  components: { DcModal  },
    name:"country",
    layout:"defaultV1",
    data() {
      return {
        modalShow: false
      }
    }

}
</script>
<style scoped>
.country-td-con{
    background: white;
    padding: 20px 20px 20px 20px;
}
/************************** MODAL  */
.modal-add-btn-initi{
    display: flex;
    align-items: center;
}
.modal-add-rec{
    margin-top: 100px;
}
</style>