function* generate(alphabet, maxLength) {
	if (maxLength <= 0) return
	for (const c of alphabet) {
		yield c
	}
	for (const c of alphabet) {
		for (const next of generate(alphabet, maxLength - 1)) {
			yield c + next
		}
	}
}

for (const c of generate('ab', 2)) {
	console.log(c)
}
