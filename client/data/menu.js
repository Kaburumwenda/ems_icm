
export const menuAccount = [
    {id:1, title: "Dashboard",page: "/",icon: "mdi mdi-home",isOpen: false,level: 0,},
	{id:2,title: "Accounts",page: "/accounts",icon: "mdi mdi-book-open-variant",isOpen: false,level: 0, 
    submenu:[ {id:1, title: "Credit", page: "/credit"}, {id:2,title: "Debit",page: "/debit"},]},
	{id:3,title: "Form", page: "/form", icon: "mdi mdi-comment-processing-outline", isOpen: false,level: 0,}
]

export const menuEvents = [
    {id:1, title: "Dashboard",page: "/dashboard/v3",icon: "mdi mdi-home",isOpen: false,level: 0,},
	{id:2,title: "Current Events",page: "/current",icon: "mdi mdi-book-open-variant",isOpen: false,level: 0, 
    submenu:[ {id:1, title: "Credit", page: "/credit"}, {id:2,title: "Debit",page: "/debit"},]},
	{id:3,title: "Latest Events", page: "/latest", icon: "mdi mdi-comment-processing-outline", isOpen: false,level: 0,}
]