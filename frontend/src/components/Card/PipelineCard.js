import { Card, CardContent, Typography } from "@mui/material"

function PipelineCard ({pipeline}) {
	return (
		<Card
			sx={{
				maxWidth: 500,
				minWidth: 280,
				backgroundColor: "#DB9D47",
				boxShadow: "1px 1px 3px #3A3042"
			}}
		>
			<CardContent>
				<Typography variant="h6" component='div'>
					{pipeline.symbol}
				</Typography>
				<div>
					<Typography variant="body1" color="text.primary">
							Sell at: {pipeline.top_value}
					</Typography>
					<Typography variant="body1" color="text.primary">
							Current Value: {pipeline.current_value}
					</Typography>
					<Typography variant="body1" color="text.primary">
							Buy at: {pipeline.bottom_value}
					</Typography>
					<Typography variant="body1" color="text.primary">
							Check Inteval: {pipeline.interval}
					</Typography>
				</div>
			</CardContent>
		</Card>
	)
}



export default PipelineCard