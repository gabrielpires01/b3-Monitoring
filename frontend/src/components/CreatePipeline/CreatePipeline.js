import { Box, Button, FormControl, InputAdornment, InputLabel, MenuItem, Select, TextField } from "@mui/material";
import { useState } from "react";
import styled from "styled-components";
import { AiOutlinePlusCircle } from "react-icons/ai"
import { createPipeline } from "../../services/api";

function CreatePipeline ({setUpdate}) {
	const [open, setOpen] = useState(false)

	const [values, setValues] = useState({
		top_value: '',
		bottom_value: '',
		symbol: '',
		email: '',
		interval: ''
	});

	const handleChange = (prop) => (event) => {
		setValues({ ...values, [prop]: event.target.value });
	};

	const handleSubmit = async () => {
		await createPipeline(values).catch(err => {
			alert(err)
		})
		setValues({
			top_value: '',
			bottom_value: '',
			symbol: '',
			email: '',
			interval: ''
		})
		setOpen(false)
		setUpdate(true)
	}

	return (
		<Component>
			<Button onClick={() => setOpen(!open)}> Create New Pipeline &nbsp;<AiOutlinePlusCircle size={30}/> </Button>
			{open && <Box
				component="form"
				sx={{
					'& .MuiTextField-root': { m: 1, width: '30ch' },
					"& .MuiFormLabel-root": {
						marginLeft: 2,
						marginTop: 2.5
					},
					display: "flex",
					flexDirection: "column",
					maxWidth: "300px"
				}}
				noValidate
				autoComplete="off"
			>
				<TextField 
					id="topValue"  
					label="Top Value" 
					onChange={handleChange("top_value")}
					placeholder="100.0000"
					InputProps={{
						startAdornment: <InputAdornment position="start">$</InputAdornment>,
					}}
					required
				/>
				<TextField 
					id="bottomValue" 
					label="Bottom Value" 
					placeholder="50.0000"
					onChange={handleChange("bottom_value")}
					InputProps={{
						startAdornment: <InputAdornment position="start">$</InputAdornment>,
					}}
					required
				/>
				<TextField id="symbol" label="Symbol to keep track" onChange={handleChange("symbol")} required/>
				<TextField id="email" label="Your email to receive Alert" onChange={handleChange("email")} required/>
				<FormControl sx={{minWidth: "200px"}}>
					<InputLabel id="demo-simple-select-label">Interval</InputLabel>
					<Select 
						onChange={handleChange("interval")} 
						value={values.interval} 
						label="Interval" 
						sx={{height: "50px"}}
						required
					>
						<MenuItem value={"1min"}>1 min</MenuItem>
						<MenuItem value={"5min"}>5 min</MenuItem>
						<MenuItem value={"15min"}>15 min</MenuItem>
						<MenuItem value={"30min"}>30 min</MenuItem>
						<MenuItem value={"60min"}>1 hour</MenuItem>
					</Select>
				</FormControl>
				<Button variant="contained" onClick={handleSubmit} >Submit</Button>
			</Box>}
		</Component>
	)
}

const Component = styled.div`
	display: flex;
	flex-direction: column;
`

export default CreatePipeline