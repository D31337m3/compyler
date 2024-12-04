from benchmark_compiler import CompilerBenchmark
import json

def main():
    benchmark = CompilerBenchmark()
    benchmark.run_benchmarks()
    
    # Export results
    with open('benchmark_results.json', 'w') as f:
        json.dump(benchmark.results, f, indent=2)
        
    # Print summary
    print("\nBenchmark Results:")
    for result in benchmark.results:
        print(f"\nFile: {result['file']}")
        print(f"Average compilation time: {result['avg_time']:.3f}s")
        print(f"Standard deviation: {result['std_dev']:.3f}s")

if __name__ == '__main__':
    main()
