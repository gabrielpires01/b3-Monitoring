import { Card, CardContent, Typography } from "@mui/material"

function QuotationCard ({time, quotation}) {
	return (
		<Card
			sx={{
				maxWidth: 500,
				minWidth: 280,
				backgroundColor: "#DB9D47",
				boxShadow: "1px 1px 3px #3A3042",
				margin: "10px",
				color: "white"
			}}
		>
			<CardContent>
				<Typography variant="h6" component='div'>
					{time}
				</Typography>
				<div>
					<Typography variant="body1" color="text.primary">
						Open Value: {quotation["1. open"]}
					</Typography>
					<Typography variant="body1" color="text.primary">
						High Value: {quotation["2. high"]}
					</Typography>
					<Typography variant="body1" color="text.primary">
						Low Value: {quotation["3. low"]}
					</Typography>
					<Typography variant="body1" color="text.primary">
						Close Value: {quotation["4. close"]}
					</Typography>
					<Typography variant="body1" color="text.primary">
						Volume: {quotation["5. volume"]}
					</Typography>
				</div>
			</CardContent>
		</Card>
	)
}

export default QuotationCard