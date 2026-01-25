// jest.config.cjs

module.exports = {
	testEnvironment: 'node',

	// The big win: stop crawling/watching irrelevant heavy folders.
	watchPathIgnorePatterns: [
		'/node_modules/',
		'/.git/',
		'/.venv/',
		'/venv/',
		'/__pycache__/',
		'/.pytest_cache/',
		'/staticfiles/',
		'/media/',
		'/coverage/',
		'/dist/',
		'/build/'
	],

	modulePathIgnorePatterns: [
		'/staticfiles/',
		'/media/',
		'/coverage/',
		'/dist/',
		'/build/'
	]
};
