import { scHelpers } from "~/assets/js/utils";
const { uniqueID } = scHelpers;



export const menuEntries = [
	{
		section_title: "Applications"
	},
	{
		id: uniqueID(),
		title: "Chat",
		icon: "mdi mdi-message-outline",
		page: "/pages/chat",
	},


	{
		id: uniqueID(),
		title: "Components",
		page: "/components",
		icon: "mdi mdi-puzzle",
		isOpen: false,
		level: 0,
		submenu:[
			{
				id: uniqueID(),
				title: "Accordion",
				page: "/components/accordion"
			},
			
		]
	},

	{
		id: uniqueID(),
		title: "Form",
		page: "/form",
		icon: "mdi mdi-puzzle",
		isOpen: false,
		level: 0,
	}
]
