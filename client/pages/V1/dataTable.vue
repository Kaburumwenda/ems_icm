
<template>
	<div id="sc-page-wrapper">
        <div id="sc-page-top-bar" class="sc-top-bar">
             <div class="sc-top-bar-content uk-flex uk-flex-1">
				<h1 class="sc-top-bar-title uk-flex-1">
					Dynamic dataTable
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
		<div id="sc-page-content">
			<div class="datatable-test-con">
              
              <table id="example" class="table table-bordered table-hover dt-responsive nowrap" style="width:100%">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>cdatetime</th>
                        <th>address</th>
                        <th>district</th>
                        <th>beat</th>
                        <th>grid</th>
                         <th>crimedescr</th>
                        <th>ucr_ncic_code</th>
                        <th>latitude</th>
                        <th>longitude</th>
                    </tr>
                </thead>
                <tbody>
                    <tr></tr>
                </tbody>
                <tfoot>
                    <tr>
                        <th>ID</th>
                        <th>cdatetime</th>
                        <th>address</th>
                        <th>district</th>
                        <th>beat</th>
                        <th>grid</th>
                         <th>crimedescr</th>
                        <th>ucr_ncic_code</th>
                        <th>latitude</th>
                        <th>longitude</th>
                    </tr>
                </tfoot>
            </table>
		</div>

        </div>
	</div>
</template>
<script>
export default {
    name:"dataTable",
    layout:"defaultV1",
    data(){
        return{
        }
    },
    mounted(){
        this.getdemoData();
    },
    methods:{           
        getdemoData(){
        let table = $('#example').DataTable({
            "processing": true,
            "serverSide": true,
            "ajax": {
                "url": "http://127.0.0.1:8000/api/v1/fakedata/?format=datatables",
                "type": "GET",
            },
            "columns": [
                { data: "id"},
                { data: "cdatetime"},
                { data: "address"},
                { data: "district"},
                { data: "beat"},
                { data: "grid"},
                { data: "crimedescr"},
                { data: "ucr_ncic_code"},
                { data: "latitude"},
                { data: "longitude"}
            ]
        });
        }
    }
}
</script>

<style>
.datatable-test-con{
    background: white;
    padding: 20px 20px 20px 20px;
}
</style>