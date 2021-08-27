<template>
    <div>
        <div id="sc-page-wrapper">
               <!-- Top navigation ***************** start *************-->
        <div id="sc-page-top-bar" class="sc-top-bar">
             <div class="sc-top-bar-content uk-flex uk-flex-1">
				<h1 class="sc-top-bar-title uk-flex-1">
					Employment Type
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
        <!-- Top Navigation ****************** end ************ -->
		<div id="sc-page-content">
        <div class="country-td-con">
            <table id="exampleaa" class="table table-bordered display dt-responsive  nowrap" style="width:100%">
                <thead>
                    <th>Employment type</th>
                    <th>Working hours</th>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            <input class="form-control" type="text" placeholder="Enter employment type">
                        </td>
                        <td>
                            <input class="form-control" type="text" placeholder="Enter Working hours">
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
export default {
    name:"employmentType",
    layout:"defaultV1",
}
</script>
<style scoped>
.country-td-con{
    background: white;
    padding: 20px 20px 20px 20px;
}
</style>