Inputs from JavaScript UI:
  Input Folder name to read scores from
  Input Score Definition
  Input Quality score filename


Functions needed from this program:
1. Read the data (in txt) from a provided input folder name, and input definition.
Example format:
{
    timestamp: xxxxxx,
    project_name: yyyyy
    quality_filename: '',
    score_filename: '',
    definition: {
        id: [0,1,2,3,4,5,6]
        race: [7],
        gender: [8],
        country: [9,10,11],
    }
}

2. Parse the data into a dataframe

3. Calculate the histogram curves, FAR/FRR curves, quality histogram

4. Save data in JSON format in a NoSQL database.

{
    timestamp: xxxxxx
    project_name: yyyyy
    none: {
        quality_boxplot: {
            mean: xxxx,
            median: yyy,
            Q1: xxxx,
            Q3: yyyy,
            IQR: zzzzz,
            top: Q3 + 1.5*IQR
            bottom: Q1 - 1.5*IQR
        },

        FAR_FRR: {
            threshold: [0,1,2,3,4,...,9999,10000],
            far: [1,1,0.99,.....,0,0],
            frr: [0,0,0.01,.....,0.99,1]
        }

        histogram: {
            bins: [0,10,20,30,...,10000]
            mated: [0,0,0,..],
            nonmated: [...,0,0,0]
        }

        EER: yyy
    }

    filter1: {
        quality_boxplot: {
            mean: xxxx,
            median: yyy,
            25%: xxxx,
            75%: yyyy,
            IQR: zzzzz,
            top: median + 1.5*IQR
            bottom: median - 1.5*IQR
        },

        FAR_FRR: {
            threshold: [0,1,2,3,4,...,9999,10000],
            far: [1,1,0.99,.....,0,0],
            frr: [0,0,0.01,.....,0.99,1]
        }

        histogram: {
            bins: [0,10,20,30,...,10000]
            mated: [0,0,0,..],
            nonmated: [...,0,0,0]
        }

        EER: yyy
    }

    filter2: {
        quality_boxplot: {
            mean: xxxx,
            median: yyy,
            25%: xxxx,
            75%: yyyy,
            IQR: zzzzz,
            top: median + 1.5*IQR
            bottom: median - 1.5*IQR
        },

        FAR_FRR: {
            threshold: [0,1,2,3,4,...,9999,10000],
            far: [1,1,0.99,.....,0,0],
            frr: [0,0,0.01,.....,0.99,1]
        }

        histogram: {
            bins: [0,10,20,30,...,10000]
            mated: [0,0,0,..],
            nonmated: [...,0,0,0]
        }

        EER: yyy
    }

    filter12: {
        quality_boxplot: {
            mean: xxxx,
            median: yyy,
            25%: xxxx,
            75%: yyyy,
            IQR: zzzzz,
            top: 75% + 1.5*IQR
            bottom: 25% - 1.5*IQR
        },

        FAR_FRR: {
            threshold: [0,1,2,3,4,...,9999,10000],
            far: [1,1,0.99,.....,0,0],
            frr: [0,0,0.01,.....,0.99,1]
        }

        histogram: {
            bins: [0,10,20,30,...,10000]
            mated: [0,0,0,..],
            nonmated: [...,0,0,0]
        }

        EER: yyy
    }
}

Filtering: filter passed to the
filter 1:
filter 2: 
