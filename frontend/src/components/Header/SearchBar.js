import {useNavigate} from "react-router-dom"
import { Box, Button, FormControl, InputLabel, MenuItem, Select, TextField } from "@mui/material"
import { useState } from "react";
import { GrSearch } from "react-icons/gr"

function SearchBar () {
	const navigate = useNavigate()
	const [values, setValues] = useState({
		symbol: '',
		interval: ''
	});

	const handleChange = (prop) => (event) => {
		setValues({ ...values, [prop]: event.target.value });
	};

	const handleSubmit = async () => {
		navigate('/quotations', {state: {symbol: values.symbol, interval: values.interval}})
		setValues({
			symbol: '',
			interval: ''
		})
	}

	return (
		<Box sx={{
			padding: 0, 
			margin: "0 !important",
			'& .MuiTextField-root': { m: 1, width: '30ch' },
			"& .MuiFormLabel-root": {
				marginLeft: 2,
				marginTop: 2.5
			},
			display: "flex",
			alignItems: "center",
			justifyContent: "center",
			flexWrap: "wrap"
		
		}}
		>
			<TextField 
				sx={{margin: "0 0 0 10px"}}
				label="symbol"
				required
				onChange={handleChange("symbol")}
			/>
			<FormControl sx={{minWidth: "200px", margin: "0 !important"}}>
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
			<Button onClick={handleSubmit}><GrSearch size="30px"/></Button>
		</Box>
	)
}


export default SearchBar