<template>
    <div>
        <div>
            <p v-if="message">
                <script>
                Swal.fire({
                    position: '',
                    icon: 'success',
                    title: 'Success',
                    text: '{{ message }}',
                    showConfirmButton: false,
                    timer: 1500
                    })
            </script>
            </p>
            <p v-else-if="error">
				<script>
					Swal.fire({
					icon: 'error',
					title: 'Oops...',
					text: '{{ error }}',
					})
				</script>
			</p>
			<p v-else-if="info">
				<script>
					Swal.fire({
					icon: 'info',
					title: 'Notice ...',
					text: '{{ info }}',
					})
				</script>
			</p>
			<p v-else></p>
        </div>
    </div>
</template>

<script>
export default {
    name:'DcMessages',

	props:{
		message:{
			type:String,
			default:null,
		},
		error:{
			type:String,
			default:null,
		},
		info:{
			type:String,
			default:null
		}
	}
}
</script>