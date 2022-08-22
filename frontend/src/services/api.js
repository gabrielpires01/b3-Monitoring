import axios from "axios"

const baseURL = "http://127.0.0.1:8000/"

export async function getPipelines() {
	const response = await axios.get(`${baseURL}`)
	return response.data
}

export async function createPipeline(body) {
	await axios.post(`${baseURL}`, body)
	return
}